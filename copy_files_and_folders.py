# coding: utf-8
import os
import stat
import shutil
import sublime
import sublime_plugin

def is_dir(path):
    """Because os.is_dir doesn't seem to exist in Sublime Text."""
    return stat.S_ISDIR(os.stat(path).st_mode)

class CopyFilesAndFoldersCommand(sublime_plugin.WindowCommand):
    def run(self, paths):
        if len(paths) != 1:
            sublime.error_message('Can only copy a single file/folder')
            return
        self.window.show_input_panel("New path:", paths[0], lambda text: self.copy(paths[0], text), None, None)

    def copy(self, source, dest):
        try:
            if is_dir(source):
                shutil.copytree(source, dest, symlinks=True)
            else:
                shutil.copy2(source, dest)
        except FileExistsError:
            sublime.error_message('Destination {dest} already exists'.format(dest=dest))
