import sublime
import sublime_plugin

class HideAutoCompleteAndExitInsertModeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def exit_insert_mode():
			self.view.run_command("exit_insert_mode")

		self.view.run_command("hide_auto_complete")
		sublime.set_timeout(exit_insert_mode, 10)

class HideAutoCompleteAndMoveUpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def move_down():
			self.view.run_command("move", {"by": "lines", "forward": False})

		self.view.run_command("hide_auto_complete")
		sublime.set_timeout(move_down, 10)

class HideAutoCompleteAndMoveDownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def move_down():
			self.view.run_command("move", {"by": "lines", "forward": True})

		self.view.run_command("hide_auto_complete")
		sublime.set_timeout(move_down, 10)
