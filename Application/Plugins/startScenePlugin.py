# startScenePlugin
# Initial code generated by Softimage SDK Wizard
# Executed Tue Mar 19 11:09:40 UTC+0800 2013 by ITAD
# 
# Tip: To add a command to this plug-in, right-click in the 
# script editor and choose Tools > Add Command.
import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
	in_reg.Author = "ITAD"
	in_reg.Name = "startScenePlugin"
	in_reg.Major = 1
	in_reg.Minor = 0

	in_reg.RegisterCommand("startScene","startScene")
	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

def startScene_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = ""
	oCmd.Tooltip = "Click to set default values when starting your scene"
	oCmd.ReturnValue = true

	return true

def startScene_Execute(  ):

	Application.LogMessage("startScene_Execute called",constants.siVerbose)
	# 
	# TODO: Put your command implementation here.
	# 
	startF = 101
	endF = 120
	
	playCtrl = Application.ActiveProject.Properties("Play Control")
	playCtrl.In = startF
	playCtrl.Out = endF
	playCtrl.GlobalIn = startF - 3
	playCtrl.GlobalOut = endF + 3
	playCtrl.Format = 8					# PAL (25 fps)
	
	capOp = Application.ActiveProject.Properties("ViewportCapture")
	capOp.Start = startF
	capOp.End = endF
	capOp.FrameRate = 25
	capOp.ImageWidth = 1920
	capOp.ImageHeight = 1080
	
	rendOp = Application.ActiveProject.ActiveScene.PassContainer.Passes("Scene Render Options")
	Application.SetValue( str(rendOp) + ".Renderer", "mental ray" )
	rendOp.FrameStart = startF
	rendOp.FrameEnd = endF
	rendOp.FramePadding = 4
	
	return true

