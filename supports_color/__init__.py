__version__ = '9.3.1'

from dict import dict as edict
from has_flag import has_flag
from os import environ as env
import platform
import re
import sys

# Ported from https://github.com/chalk/supports-color/blob/main/index.js

if has_flag('no-color') or \
        has_flag('no-colors') or \
        has_flag('color=false') or \
        has_flag('color=never'):
    flagForceColor = 0
elif has_flag('color') or \
        has_flag('colors') or \
        has_flag('color=true') or \
        has_flag('color=always'):
    flagForceColor = 1
else:
    flagForceColor = None


def envForceColor():
    if 'FORCE_COLOR' in env:
        if env.get('FORCE_COLOR') == 'true':
            return 1

        if env.get('FORCE_COLOR') == 'false':
            return 0

        return 1 if len(env.get('FORCE_COLOR')) == 0 else min(int(env.get('FORCE_COLOR'), 10), 3)


def translateLevel(level):
    if level == 0:
        return False

    return edict(
        level=level,
        hasBasic=True,
        has256=level >= 2,
        has16m=level >= 3
    )


# function _supportsColor(haveStream, {streamIsTTY, sniffFlags = true} = {}) {
def _supportsColor(haveStream, *, streamIsTTY, sniffFlags=True):
    global flagForceColor
    # const noFlagForceColor = envForceColor();
    noFlagForceColor = envForceColor()
    # if (noFlagForceColor !== undefined) {
    #     flagForceColor = noFlagForceColor;
    # }
    if noFlagForceColor is not None:
        flagForceColor = noFlagForceColor
    #
    # const forceColor = sniffFlags ? flagForceColor : noFlagForceColor;
    forceColor = flagForceColor if sniffFlags else noFlagForceColor
    #
    # if (forceColor === 0) {
    #     return 0;
    # }
    if forceColor == 0:
        return 0
    #
    # if (sniffFlags) {
    #     if (hasFlag('color=16m') ||
    #         hasFlag('color=full') ||
    #         hasFlag('color=truecolor')) {
    #         return 3;
    #     }
    #
    #     if (hasFlag('color=256')) {
    #         return 2;
    #     }
    # }
    if sniffFlags:
        if has_flag('color=16m') or \
                has_flag('color=full') or \
                has_flag('color=truecolor'):
            return 3

        if has_flag('color=256'):
            return 2
    #
    # if (haveStream && !streamIsTTY && forceColor === undefined) {
    #     return 0;
    # }
    if haveStream and not streamIsTTY and forceColor is None:
        return 0
    #
    # const min = forceColor || 0;
    min = forceColor or 0
    # if (env.TERM === 'dumb') {
    #     return min;
    # }
    if env.get('TERM') == 'dumb':
        return min

    # if (process.platform === 'win32') {
    #     // Windows 10 build 10586 is the first Windows release that supports 256 colors.
    #     // Windows 10 build 14931 is the first release that supports 16m/TrueColor.
    #     const osRelease = os.release().split('.');
    #     if (
    #         Number(osRelease[0]) >= 10 &&
    #         Number(osRelease[2]) >= 10586
    #     ) {
    #         return Number(osRelease[2]) >= 14931 ? 3 : 2;
    #     }
    #
    #     return 1;
    # }
    if sys.platform == 'win32':
        osRelease = platform.version().split('.')
        if int(osRelease[0]) > 10 and int(osRelease[2] >= 10586):
            if int(osRelease[2] >= 14931):
                return 3
            else:
                return 2
        return 1

    # if ('CI' in env) {
    #     if ('GITHUB_ACTIONS' in env) {
    #         return 3;
    #     }
    #
    #     if (['TRAVIS', 'CIRCLECI', 'APPVEYOR', 'GITLAB_CI', 'BUILDKITE', 'DRONE'].some(sign => sign in env) || env.CI_NAME === 'codeship') {
    #         return 1;
    #     }
    #
    #     return min;
    # }
    if 'CI' in env:
        if 'GITHUB_ACTIONS' in env:
            return 3

        if any([sign in env for sign in
                ['TRAVIS', 'CIRCLECI', 'APPVEYOR', 'GITLAB_CI', 'BUILDKITE', 'DRONE']]) or env.get(
            'CI_NAME') == 'codeship':
            return 1

    # if ('TEAMCITY_VERSION' in env) {
    #     return /^(9\.(0*[1-9]\d*)\.|\d{2,}\.)/.test(env.TEAMCITY_VERSION) ? 1 : 0;
    # }
    if 'TEAMCITY_VERSION' in env:
        if re.search(r'^(9\.(0*[1-9]\d*)\.|\d{2,}\.)', env.get('TEAMCITY_VERSION'), re.IGNORECASE):
            return 1
        else:
            return 0

    # if (env.COLORTERM === 'truecolor') {
    #     return 3;
    # }
    if env.get('COLORTERM') == 'truecolor':
        return 3

    # if (env.TERM === 'xterm-kitty') {
    #     return 3;
    # }
    if env.get('TERM') == 'xterm-kitty':
        return 3

    # Fix for iTerm2 via SSH
    if env.get('LC_TERMINAL') == 'iTerm2':
        return 3

    #
    # if ('TERM_PROGRAM' in env) {
    #     const version = Number.parseInt((env.TERM_PROGRAM_VERSION || '').split('.')[0], 10);
    #
    #     switch (env.TERM_PROGRAM) {
    #         case 'iTerm.app':
    #             return version >= 3 ? 3 : 2;
    #         case 'Apple_Terminal':
    #             return 2;
    #         // No default
    #     }
    # }
    if 'TERM_PROGRAM' in env:
        version = int(env.get('TERM_PROGRAM_VERSION', '0').split('.')[0], 10)

        if env.get('TERM_PROGRAM') == 'iTerm.app':
            return 3 if version >= 3 else 2
        if env.get('TERM_PROGRAM') == 'Apple_Terminal':
            return 2
    #
    # if (/-256(color)?$/i.test(env.TERM)) {
    #     return 2;
    # }
    if 'TERM' in env:
        if re.search(r'-256(color)?$', env.get('TERM'), re.IGNORECASE):
            return 2
        #
        # if (/^screen|^xterm|^vt100|^vt220|^rxvt|color|ansi|cygwin|linux/i.test(env.TERM)) {
        #     return 1;
        # }
        if re.search(r'^screen|^xterm|^vt100|^vt220|^rxvt|color|ansi|cygwin|linux', env.get('TERM'), re.IGNORECASE):
            return 1
    #
    # if ('COLORTERM' in env) {
    #     return 1;
    # }
    if 'COLORTERM' in env:
        return 1
    #
    # return min;
    return min


# export function createSupportsColor(stream, options = {}) {
def createSupportsColor(stream, **options):
    # const level = _supportsColor(stream, {
    # 	streamIsTTY: stream && stream.isTTY,
    # 	...options
    # });
    level = _supportsColor(stream, streamIsTTY=stream and stream.isatty(), **options)
    #
    # return translateLevel(level);
    return translateLevel(level)


# const supportsColor = {
#   stdout: createSupportsColor({isTTY: tty.isatty(1)}),
#   stderr: createSupportsColor({isTTY: tty.isatty(2)})
# }

supportsColor = edict(
    stdout=createSupportsColor(sys.stdout),
    stderr=createSupportsColor(sys.stderr),
)
