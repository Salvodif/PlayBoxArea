$web = Get-SPWeb http://nevecrino:26295
$listname = Read-Host "Give me the list name"
$list =  $web.Lists[$listname]
#$listItems = $list.Items

#$item = $listItems[0]

clear

#foreach ($field in $item.Fields) {
#	$fieldData = @{ InternalName = $field.InternalName; StaticName = $field.StaticName; Title = $field.Title }
#	$fieldData | Format-Table Name,Value -Auto
#}

foreach ($field in $list.Fields) {
	$fieldData = @{ InternalName = $field.InternalName; StaticName = $field.StaticName; Title = $field.Title; GUID = $field.Id }
	$fieldData | Format-Table Name,Value -Auto
}
