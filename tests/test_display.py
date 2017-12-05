import display


def test_display_help_with_command_help():
    expected_help_list = """\x1b[1mhelp\n----\x1b[0m\nCommand: help\nDescription: List commands and their brief descriptions\nArguments: None\n\nCommand: help <command>\nDescription: Show verbose description of usage and show valid arguments for <command>\nArguments: <command>: Command to show description and valid arguments for.\nCan be any of the following:\n\thelp\n\tget\n\tconfig\n\tlist\n\tanalyze\n\tquit\n"""
    help_list = display.display_help_with_command("help")
    assert repr(help_list) == repr(expected_help_list)


def test_display_help_help():
    expected_display_help = """\x1b[1mhelp\n----\x1b[0m\nCommand: help\nDescription: List commands and their brief descriptions\nArguments: None\n\nCommand: help <command>\nDescription: Show verbose description of usage and show valid arguments for <command>\nArguments: <command>: Command to show description and valid arguments for.\nCan be any of the following:\n\thelp\n\tget\n\tconfig\n\tlist\n\tanalyze\n\tquit\n"""
    display_help = display.display_help_help()
    assert repr(display_help) == repr(expected_display_help)


def test_display_get_help():
    expected_get_help = """\x1b[1mget\n----\x1b[0m\nCommand: get\nDescription: Downloads repositories from Project with specified Prefix to directory Out\nArguments: None\n"""
    get_help = display.display_get_help()
    assert repr(get_help) == repr(expected_get_help)


def test_display_config_help():
    expected_config_help = """\x1b[1mconfig\n----\x1b[0m\nCommand: config\nDescription: show the values in the config file\nArguments: None\n\nCommand: config edit\nDescription: Edit or reset the values in the config file\nArguments: <option>\n"""
    config_help = display.display_config_help()
    assert repr(config_help) == repr(expected_config_help)


def test_display_list_help():
    expected_list_help = """\x1b[1mlist\n----\x1b[0m\nCommand: list\nDescription: List all repositories\nArguments: None\n\nCommand: list <repo name>\nDescription: Lists all files in the given repository\nArguments: <repo name>\n"""
    list_help = display.display_list_help()
    assert repr(list_help) == repr(expected_list_help)


def test_display_analyze_help():
    expected_analyze_help = """\x1b[1manalyze\n----\x1b[0m\nCommand: analyze <target>\nDescription: Performs analysis for specified target ('source','comments','commits','reflection')\nArguments: <target>\n"""
    analyze_help = display.display_analyze_help()
    assert repr(analyze_help) == repr(expected_analyze_help)


def test_display_quit_help():
    expected_quit_help = """\x1b[1mquit\n----\x1b[0m\nCommand: quit\nDescription: Quits the Accelegator program\nArguments: None\n"""
    quit_help = display.display_quit_help()
    assert repr(quit_help) == repr(expected_quit_help)
