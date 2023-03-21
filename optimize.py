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
