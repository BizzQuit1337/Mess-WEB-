
while not ended:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            ended = True
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                block.text_align = (block.text_align + 1) % 2  # switch text align
            elif ev.key == pygame.K_SPACE:
                block.text = ALT_TXT
        elif ev.type == pygame.KEYUP:
            if not pygame.key.get_pressed()[pygame.K_SPACE]:
                block.text = INIT_TXT
    screen.fill('white')
    block.draw(screen)
    kengi.core.display_update()
kengi.core.cleanup()
[root@bladebox src]# pwd
/srv/httpd/html/brython-runner/kengi-main/src
[root@bladebox src]# cp /srv/httpd/html/brython-runner/kengi-main/src/min-example-gui.py /srv/httpd/html/brython-runner/kengi-main/src/min-example-gui.py.backup
[root@bladebox src]# nano min-example-gui.py
[root@bladebox src]# [root@bladebox src]# nano min-example-gui.py
[root@bladebox src]# [root@bladebox src]# cd katagames_engine
[root@bladebox katagames_engine]# ls
_BaseGameState.py  foundation  _hub.pyc     __init__.pyc  _sm_shelf  __version__.py
caps               _hub.py     __init__.py  __pycache__   _util.py
[root@bladebox katagames_engine]# cd
[root@bladebox ~]# cd ..
[root@bladebox /]# cd /usr/local/lib64/python3.6/site-packages
[root@bladebox site-packages]# ls
cv2                                       opencv_contrib_python_headless-4.4.0.46.dist-info  pygame
numpy                                     opencv_contrib_python_headless.libs                pygame-2.1.2.dist-info
numpy-1.19.5.dist-info                    opencv_contrib_python.libs                         pygame.libs
numpy.libs                                opencv_python-4.4.0.46.dist-info
opencv_contrib_python-4.4.0.46.dist-info  opencv_python.libs
[root@bladebox site-packages]# pwd
/usr/local/lib64/python3.6/site-packages
[root@bladebox site-packages]# cd pygmae
-bash: cd: pygmae: No such file or directory
[root@bladebox site-packages]# cat pygame
cat: pygame: Is a directory
[root@bladebox site-packages]# cd pygame
[root@bladebox pygame]# ls
base.cpython-36m-x86_64-linux-gnu.so         math.cpython-36m-x86_64-linux-gnu.so
bufferproxy.cpython-36m-x86_64-linux-gnu.so  math.pyi
bufferproxy.pyi                              midi.py
_camera.cpython-36m-x86_64-linux-gnu.so      midi.pyi
_camera_opencv.py                            mixer.cpython-36m-x86_64-linux-gnu.so
camera.py                                    mixer_music.cpython-36m-x86_64-linux-gnu.so
camera.pyi                                   mixer.pyi
_camera_vidcapture.py                        mouse.cpython-36m-x86_64-linux-gnu.so
color.cpython-36m-x86_64-linux-gnu.so        mouse.pyi
colordict.py                                 music.pyi
color.pyi                                    newbuffer.cpython-36m-x86_64-linux-gnu.so
_common.pyi                                  pixelarray.cpython-36m-x86_64-linux-gnu.so
constants.cpython-36m-x86_64-linux-gnu.so    pixelarray.pyi
constants.pyi                                pixelcopy.cpython-36m-x86_64-linux-gnu.so
cursors.py                                   pixelcopy.pyi
cursors.pyi                                  pkgdata.py
display.cpython-36m-x86_64-linux-gnu.so      __pycache__
display.pyi                                  pygame.ico
docs                                         pygame_icon.bmp
draw.cpython-36m-x86_64-linux-gnu.so         pygame_icon.icns
draw.pyi                                     pygame_icon_mac.bmp
draw_py.py                                   __pyinstaller
event.cpython-36m-x86_64-linux-gnu.so        pypm.cpython-36m-x86_64-linux-gnu.so
event.pyi                                    py.typed
examples                                     rect.cpython-36m-x86_64-linux-gnu.so
fastevent.py                                 rect.pyi
fastevent.pyi                                rwobject.cpython-36m-x86_64-linux-gnu.so
font.cpython-36m-x86_64-linux-gnu.so         scrap.cpython-36m-x86_64-linux-gnu.so
font.pyi                                     scrap.pyi
freesansbold.ttf                             _sdl2
_freetype.cpython-36m-x86_64-linux-gnu.so    sndarray.py
freetype.py                                  sndarray.pyi
freetype.pyi                                 _sprite.cpython-36m-x86_64-linux-gnu.so
ftfont.py                                    sprite.py
gfxdraw.cpython-36m-x86_64-linux-gnu.so      sprite.pyi
gfxdraw.pyi                                  surface.cpython-36m-x86_64-linux-gnu.so
image.cpython-36m-x86_64-linux-gnu.so        surface.pyi
imageext.cpython-36m-x86_64-linux-gnu.so     surfarray.py
image.pyi                                    surfarray.pyi
__init__.py                                  surflock.cpython-36m-x86_64-linux-gnu.so
__init__.pyi                                 sysfont.py
joystick.cpython-36m-x86_64-linux-gnu.so     tests
joystick.pyi                                 threads
key.cpython-36m-x86_64-linux-gnu.so          time.cpython-36m-x86_64-linux-gnu.so
key.pyi                                      time.pyi
locals.py                                    transform.cpython-36m-x86_64-linux-gnu.so
macosx.py                                    transform.pyi
mask.cpython-36m-x86_64-linux-gnu.so         version.py
mask.pyi                                     version.pyi
[root@bladebox pygame]# clear
[root@bladebox pygame]# cd
[root@bladebox ~]# cd ..
[root@bladebox /]# cd /srv/httpd/html/brython-runner/kengi-main/src
[root@bladebox src]# ls
alphbeta.ttf  game_templates    min-example-gui.py         min-example-kengiOn.py  requirements.txt
build         katagames_engine  min-example-gui.py.backup  min-example-mvc.py      setup.py
examples      MANIFEST.in       min-example-kengiOff.py    python
[root@bladebox src]# cd katagames_engine
[root@bladebox katagames_engine]# ls
_BaseGameState.py  foundation  _hub.pyc     __init__.pyc  _sm_shelf  __version__.py
caps               _hub.py     __init__.py  __pycache__   _util.py
[root@bladebox katagames_engine]# ls -lsa
total 32
0 drwxrwxrwx 6 root root  205 Mar 16 09:09 .
4 drwxrwxrwx 6 root root 4096 Mar 16 09:12 ..
4 -rw-r--r-- 1 root root  673 Mar 15 10:19 _BaseGameState.py
0 drwxrwxrwx 6 root root   94 Mar 15 10:19 caps
0 drwxrwxrwx 3 root root   91 Mar 16 08:20 foundation
4 -rw-r--r-- 1 root root 1614 Mar 16 08:16 _hub.py
4 -rw-r--r-- 1 root root 2573 Mar 16 09:08 _hub.pyc
4 -rw-r--r-- 1 root root 1902 Mar 16 09:03 __init__.py
4 -rw-r--r-- 1 root root 2629 Mar 16 09:08 __init__.pyc
0 drwxr-xr-x 2 root root  163 Mar 16 09:03 __pycache__
0 drwxrwxrwx 6 root root  141 Mar 15 10:19 _sm_shelf
4 -rw-r--r-- 1 root root  305 Mar 15 10:19 _util.py
4 -rw-r--r-- 1 root root  471 Mar 15 10:19 __version__.py
[root@bladebox katagames_engine]# cat _BaseGameState.py
from abc import ABCMeta, abstractmethod


class BaseGameState(metaclass=ABCMeta):

    def __init__(self, state_ident, state_name):
        self.__state_ident = state_ident
        self.__state_name = state_name

    @abstractmethod
    def enter(self):
        pass

    def get_id(self):
        return self.__state_ident

    def get_name(self):
        return self.__state_name

    def pause(self):
        print(self.__class__.__name__)
        raise AssertionError('not meant to be paused')

    @abstractmethod
    def release(self):
        pass

    def resume(self):
        print(self.__class__.__name__)
        raise AssertionError('not meant to be resumed')
[root@bladebox katagames_engine]# ls
_BaseGameState.py  foundation  _hub.pyc     __init__.pyc  _sm_shelf  __version__.py
caps               _hub.py     __init__.py  __pycache__   _util.py
[root@bladebox katagames_engine]# cat __init__.py
"""
Author: github.com/wkta
Principles: The ultimate engine
-------------------------------
 * is a wrapper around pygame functions & objects

 * runs best within the KataSDK but can also be detached and runs independently.
 Just rename _engine -> engine, and Voila

 * does not know ANYTHING about whether it runs in web ctx or not.
 The engine can be "hacked" so it runs a pygame emulator instead of pygame,
 but this does not change anythin' to engine's implementation per se

 * is extensible: engine needs to be able to receive extensions like a GUI manager,
 an isometric engine, etc. without any architecture change.
 To achieve this we will use the same hacking method as previously,
 basically this is like using an Injector (relates to-> Dependency Injection pattern)
 that is:
 if an extension module is called it will be searched/fetched via the Injector.
 This searching is done via __getattr__(name) and the _available_sub_modules dict. structure

"""
from . import _hub
from ._BaseGameState import BaseGameState
from ._util import underscore_format, camel_case_format
from .foundation import defs

from .__version__ import ENGI_VERSION as vernum
_hub.registered_vernum = vernum


def plugin_bind(extname, pypath):
    _hub.instance.alert_if_needed()
    _hub.Injector.register_plugin(extname, pypath)


def bulk_plugin_bind_op(assoc_extname_pypath):
    _hub.instance.alert_if_needed()
    for ename, pypath in assoc_extname_pypath.items():
        _hub.Injector.register_plugin(ename, pypath)


def __getattr__(targ_sm_name):
    if targ_sm_name not in _hub.extra_sm.keys():
        raise KeyError('sub-module "{}" you request from Kengi cannot be found!'.format(targ_sm_name))
    else:
        try:
            return getattr(_hub, targ_sm_name)
        except AttributeError:
            raise AttributeError("(kengi injector) _hub has no valid attribute '{}'".format(targ_sm_name))