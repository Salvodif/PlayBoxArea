$web = get-spweb http://nevecrino:26295
$contenttypes = $web.ContentTypes

foreach ($contenttype in $contenttypes) {
Write-Host $contenttype.Name $contenttype.Id | Format-Table -AutoSize
}

Read-Host