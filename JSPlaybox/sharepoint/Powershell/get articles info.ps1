$web = Get-SPWeb http://nevecrino:26295
$list = $web.Lists["Pages"]

$spQuery = New-Object Microsoft.SharePoint.SPQuery
$spQuery.RowLimit = 2000
$caml = '<Where><Eq><FieldRef Name=''ContentType''/><Value Type=''Text''>Article Page</Value></Eq></Where>'
$spQuery.Query = $caml 

$listItems = $list.GetItems($spQuery)

foreach ($item in $listItems) {
	foreach ($field in $item.Fields) {
		Write-Host $field.Title " - " $item[$field.InternalName] 
	}

	Write-Host "========================================================================================="
}