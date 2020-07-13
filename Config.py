from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')
config.remove_section('settings')


config.add_section('settings')

#set default settings below
#if any new settings added, add the same in ScreenMarkerPro.py file during load settings and save_settings() function
config.set('settings', 'pen_size', '5' )
config.set('settings', 'highlighter_size', '20')
config.set('settings', 'highlighter_transparency', '0.5')
config.set('settings', 'eraser_size', '10')
config.set('settings', 'pointer_size', '20')
config.set('settings', 'text_size', 'Red')
config.set('settings', 'board_width', '600')
config.set('settings', 'board_height', '600')


config.set('settings', 'pen_color', 'Blue')
config.set('settings', 'highlighter_color', 'Yellow')
config.set('settings', 'board_color', 'White')
config.set('settings', 'pointer_color', 'Red')
config.set('settings', 'shape_color', 'Red')
config.set('settings', 'text_color', 'Red')


config.set('settings', 'toolbox_visible', 'False')
config.set('settings', 'toolbox_verticle', 'True')
config.set('settings', 'shape_fill', 'False')
config.set('settings', 'fullscreen_board', 'True')
config.set('settings', 'pointer_enable', 'True')


with open('config.ini', 'w') as f:
    config.write(f)