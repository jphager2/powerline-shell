from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 5
    USERNAME_BG = 7
    USERNAME_ROOT_BG = 7

    HOSTNAME_FG = 5
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 7
    PATH_FG = 5
    CWD_FG = 5
    SEPARATOR_FG = 5

    READONLY_BG = 7
    READONLY_FG = 5

    REPO_CLEAN_BG = 7
    REPO_CLEAN_FG = 7
    REPO_DIRTY_BG = 7
    REPO_DIRTY_FG = 7

    GIT_AHEAD_BG = 7
    GIT_AHEAD_FG = 5
    GIT_BEHIND_BG = 7
    GIT_BEHIND_FG = 5
    GIT_STAGED_BG = 7
    GIT_STAGED_FG = 5
    GIT_NOTSTAGED_BG = 7
    GIT_NOTSTAGED_FG = 5
    GIT_UNTRACKED_BG = 7
    GIT_UNTRACKED_FG = 5
    GIT_CONFLICTED_BG = 7
    GIT_CONFLICTED_FG = 5
    GIT_STASH_BG = 7
    GIT_STASH_FG = 5

    JOBS_FG = 5
    JOBS_BG = 7

    CMD_PASSED_BG = 7
    CMD_PASSED_FG = 5
    CMD_FAILED_BG = 7
    CMD_FAILED_FG = 5

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 7
    VIRTUAL_ENV_FG = 5

    AWS_PROFILE_FG = 5
    AWS_PROFILE_BG = 0

    TIME_FG = 5
    TIME_BG = 7
