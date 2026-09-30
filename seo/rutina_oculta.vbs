' Lanza la rutina SEO diaria de Claude sin abrir ninguna ventana (0 = oculta).
Set sh = CreateObject("WScript.Shell")
carpeta = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
sh.Run "cmd /c """ & carpeta & "\rutina_diaria.bat""", 0, False
