import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("outlook")
shell.AppActivate("Outlook")
shell.SendKeys("^o", 0) # 1 für Pause = true 0 für nein
shell.SendKeys("^a", 0)
shell.SendKeys("^c", 0)