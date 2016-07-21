<?php 
include('bijoy2unicode.php');

$input_text = isset($_GET['text'])?$_GET['text']:'';
$output_text = '';
if($input_text){
	$output_text = convertBijoyToUnicode($input_text);
}
?>
<html>
	<head>
		<title>Bijoy to unicode converter</title>
		<meta http-equiv=Content-Type content="text/html; charset=UTF-8">
		<meta charset="UTF-8">
	</head>
	<body>
		<h1>Bijoy to unicode converter</h1>
		<form action="">
			Input: 
			<textarea name="text"><?php echo $input_text?></textarea>
			<input type="submit" value="submit" />
		</form>
		Output: 
		<p><?php echo $output_text?></p>
	</body>
</html>