$siteUrl = Read-Host "Site url"
$site = Get-SPSite $siteUrl
$uri = Read-Host "Uri document"

$serviceCtx = Get-SPServiceContext -Site $site
$socialRatingMgr = New-Object Microsoft.Office.Server.SocialData.SocialRatingManager($serviceCtx)
$rating = $socialRatingMgr.GetRating($uri)

$rating | Format-Table -AutoSize -Wrap

$site.Dispose()