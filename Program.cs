namespace PrerequisiteInstaller
{
    using System;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;
    using System.Net;
    public class InstallPrerequisites
    {
        public static class Constants
        {
            // Define global constants
            public const string logFileName = "PrerequisiteInstallerLog.txt";
            public const string logWriteError = "Couldn't write to log!";
            public const string downloadDirectory = "PrerequisiteInstaller_Downloads";
        }
        private static void Log(string logText)
        {
            try
            {
                //Write to log
                using (StreamWriter w = File.AppendText(Constants.logFileName))
                {
                    w.WriteLine(logText);
                }
            }

            catch (Exception e)
            {
                PrintError(e, Constants.logWriteError, true);
            }
        }

        private static void PrintError(Exception e, string errorMessage, bool fatal)
        {
            string enterAction = "continue";
            string logPrefix = "";

            //Print [FATAL] tag
            if (fatal)
            {
                enterAction = "quit";
                Console.Write("[FATAL]");
                logPrefix = "[FATAL]";
            }

            //Print [ERROR] and message
            Console.WriteLine("[ERROR] " + errorMessage);
            Console.WriteLine(e.Message);
            Console.WriteLine("\nPress Enter to " + enterAction + "...");

            //Log error
            if (errorMessage != Constants.logWriteError)
                Log(String.Concat(logPrefix, "[ERROR] " + errorMessage + " (" + e.Message + ")"));

            //Press Enter to continue or quit
            Console.ReadLine();
            if (errorMessage != Constants.logWriteError)
                Log("[USER] User pressed Enter to " + enterAction);
            if (fatal)
                System.Environment.Exit(1);
        }

        public static void Main(string[] args)
        {
            string version = "1.2.1";

            //Reset log
            if (File.Exists(Constants.logFileName))
                try
                {
                    File.Delete(Constants.logFileName);
                }

                catch (Exception e)
                {
                    PrintError(e, "Couldn't reset log file!", true);
                }

            //Create new log
            Log("v" + version);
            Log("[INFO] Created new log on " + DateTime.Now);

            //Set up variables
            string[] fileURLs = new string[] {
                "https://aka.ms/vs/16/release/VC_redist.x64.exe",
                "https://aka.ms/vs/16/release/VC_redist.x86.exe",
                "https://download.visualstudio.microsoft.com/download/pr/6a9318dd-fec5-4df3-84df-ffd917b382ea/d3391ca5a4e14a8a96e04bbfa5c4c2dc/windowsdesktop-runtime-3.1.29-win-x64.exe",
                "https://download.visualstudio.microsoft.com/download/pr/3aa4e942-42cd-4bf5-afe7-fc23bd9c69c5/64da54c8864e473c19a7d3de15790418/windowsdesktop-runtime-5.0.17-win-x64.exe",
                "https://download.visualstudio.microsoft.com/download/pr/b6fe5f2a-95f4-46f1-9824-f5994f10bc69/db5ec9b47ec877b5276f83a185fdb6a0/windowsdesktop-runtime-5.0.17-win-x86.exe",
                "https://download.visualstudio.microsoft.com/download/pr/fe8415d4-8a35-4af9-80a5-51306a96282d/05f9b2a1b4884238e69468e49b3a5453/windowsdesktop-runtime-6.0.9-win-x64.exe",
                "https://download.visualstudio.microsoft.com/download/pr/925f9407-2767-4341-857a-43cdfad71e17/0b84db913bdbb1dcf02db937a3cd3f63/windowsdesktop-runtime-6.0.9-win-x86.exe"
            };

            int fileCount = fileURLs.Count();
            int downloadSuccessCount = 0;
            int installSuccessCount = 0;
            Process myProcess = new Process();

            //Intro
            Console.WriteLine("P4G PC All-in-One Prerequisite Installer v" + version + "\nby Pixelguin\n");
            Console.WriteLine("This program will download and run " + fileCount + " installers, one after the other.\nJust follow the instructions in this window.\n\nPress Enter to start.");

            Console.ReadLine();
            Log("[USER] User pressed Enter to start downloading");

            //Create directory
            if (!Directory.Exists(Constants.downloadDirectory))
            {
                Directory.CreateDirectory(Constants.downloadDirectory);
                Console.WriteLine("Created " + Constants.downloadDirectory + " directory. Don't delete this!\nThe program will delete the directory automatically at the end.\n");
                Log("[INFO] Created " + Constants.downloadDirectory + " directory");
            }

            //Download files
            using (var client = new WebClient())
            {
                for (var i = 0; i < fileURLs.Count(); i++)
                {
                    //Set file name
                    string fileName = System.IO.Path.GetFileName(fileURLs[i]);

                    try
                    {
                        string downloadText = "Downloading " + fileName + " (" + (i + 1) + "/" + fileCount + ")";

                        //Output to log and console
                        Console.Write(downloadText + "...");
                        Log("[INFO] " + downloadText + " from " + fileURLs[i]);

                        //Download the file
                        client.DownloadFile(fileURLs[i], Constants.downloadDirectory + "\\" + fileName);

                        Console.WriteLine("Done!");
                        Log("[INFO] Download successful, downloadSuccessCount = " + ++downloadSuccessCount);
                    }

                    catch (Exception e)
                    {
                        PrintError(e, "Couldn't download " + fileName + "!", false);
                    }
                }
            }

            //Create array of files in downloads directory
            string[] files = Directory.GetFiles(Constants.downloadDirectory);

            //Install files
            for (var i = 0; i < files.Count(); i++)
            {
                var fileName = files[i];

                try
                {
                    //Output to console and log
                    Console.Clear();
                    string launchText = "Launching " + fileName + " (" + (i + 1) + "/" + fileCount + ")";

                    Console.WriteLine(new string('=', launchText.Length + 3));
                    Console.WriteLine(launchText + "...");
                    Console.WriteLine(new string('=', launchText.Length + 3));
                    Log("[INFO] " + launchText);

                    /*String for options that appear depending if the user has already installed the program + next steps to take
                      Not currently very interesting but may be useful in the future if files change */
                    string notInstalledButtons = "Install/Close";
                    string alreadyInstalledButtons = "Repair/Uninstall/Close";
                    string alreadyInstalledActions = "Close -> Yes";

                    if (fileName.Contains("VC_redist"))
                    {
                        Console.WriteLine("\nFollow the installer's instructions.");
                        Console.WriteLine("\nIf you get a \"Setup Failed - 0x80070666\" error, you already have this runtime installed.\nClick Close and the program will continue.");
                    }
                    else
                    {
                        Console.WriteLine("\nIf the options given to you are " + alreadyInstalledButtons + ", you already have this installed.\nClick " + alreadyInstalledActions + " and the program will continue.");
                        Console.WriteLine("\nOtherwise, you should see " + notInstalledButtons + " - follow the installer's instructions.");
                    }

                    //Launch installer and wait for it to close
                    myProcess.StartInfo.FileName = fileName;
                    myProcess.Start();
                    myProcess.WaitForExit();
                    Log("[INFO] Run successful, installSuccessCount = " + ++installSuccessCount);
                }

                catch (Exception e)
                {
                    PrintError(e, "Couldn't run " + fileName + "!", false);
                }
            }

            //Wrap-up output to log and console
            Console.Clear();

            string outputText = "Successfully downloaded " + downloadSuccessCount + "/" + fileCount + " files!";
            Console.WriteLine(outputText);
            Log("[INFO] " + outputText);

            outputText = "Successfully ran " + installSuccessCount + "/" + fileCount + " installers!";
            Console.WriteLine(outputText);
            Log("[INFO] " + outputText);

            //Delete downloads directory
            try
            {
                Directory.Delete(Constants.downloadDirectory, true);
                Console.WriteLine("Successfully deleted " + Constants.downloadDirectory + " directory!");
                Log("[INFO] Deleted " + Constants.downloadDirectory + " directory");
            }

            catch (Exception e)
            {
                PrintError(e, "Couldn't delete " + Constants.downloadDirectory + " directory!", false);
            }

            Console.WriteLine("\nPress Enter to exit...");
            Console.ReadLine();
            Log("[USER] User pressed Enter to exit");
        }
    }
}