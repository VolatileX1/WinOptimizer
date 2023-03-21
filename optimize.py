Set-ExecutionPolicy Unrestricted -Force

# Clean Junk Files

Get-ChildItem -Path "$env:windir\Temp" -Recurse | Remove-Item -Force -Recurse
Get-ChildItem -Path "$env:USERPROFILE\AppData\Local\Temp" -Recurse | Remove-Item -Force -Recurse
Get-ChildItem -Path "$env:windir\SoftwareDistribution\Download" -Recurse | Remove-Item -Force -Recurse
Clear-RecycleBin -Force

# Clean Temporary Folders

Remove-Item -Path "$env:windir\Prefetch" -Force -Recurse
Remove-Item -Path "$env:windir\Logs" -Force -Recurse
Remove-Item -Path "$env:windir\InfusedApps" -Force -Recurse
Remove-Item -Path "$env:windir\Microsoft.NET\Framework\v*\Temporary ASP.NET Files" -Force -Recurse

# Clean Cache

Clear-DnsClientCache
Clear-HostCache
Clear-JournalingReceiveFolder
Clear-MsolMfaDeviceCache
Clear-MsolUserDeviceProfile
Clear-MsolUserFeatureFlagCache
Clear-NetNeighbor
Clear-RDMSession
Clear-Tpm
Clear-Variable -Name Function:\* -ErrorAction SilentlyContinue

  # Optimize Registry

Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -Name DisablePagingExecutive -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -Name LargeSystemCache -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -Name IoPageLockLimit -Value 8192 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" -Name SystemResponsiveness -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name NtfsDisable8dot3NameCreation -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\DWM" -Name EnableMachineCheck -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name CoolSwitch -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name ForegroundFlashCount -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name MenuShowDelay -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name CursorBlinkRate -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name UserPreferencesMask -Value 90 12 03 80 -Type Binary
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name DisableTaskOffload -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name DisableBandwidthThrottling -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name SizReqBuf -Value 16777216 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name Size -Value 3 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters" -Name NoNameReleaseOnDemand -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name TcpMaxDataRetransmissions -Value 5 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name DontUsePowerShellOnWinX -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Safer\CodeIdentifiers" -Name AuthenticatedCodePolicy -Value 0 -Type DWord

# Other Possible Tweaks

Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name DisableCMD -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name DisableRegistryTools -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name DisableTaskMgr -Value 1 -Type DWord
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name HideFileExt -Value 1 -Type DWord
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name ShowSuperHidden -Value 1 -Type DWord
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name Start_ShowMyGames -Value 0 -Type DWord
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name MouseHoverTime -Value 50 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name GlobalMaxTcpWindowSize -Value 65535 -Type DWord
