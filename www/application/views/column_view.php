<script type="text/javascript">

Element.addMethods({
  scrollTo: function(element, left, top){
    var element = $(element);
    if (arguments.length == 1){
      var pos = element.cumulativeOffset();
      window.scrollTo(pos[0], pos[1]);
    } else {
      element.scrollLeft = left;
      element.scrollTop  = top;
    }
    return element;
  }
});

	$('c<?= $column; ?>in').setStyle({left:($('c<?= $column; ?>in').up(0).previous(0).positionedOffset().left+$('c<?= $column; ?>in').up(0).previous(0).getWidth()+'px')});
	$('c<?= $column; ?>').show();
	$('scrollto').scrollTo(1011,1);

</script>
<div id="c<?= $column; ?>in" class="right_frame_column">

<?php 
	$row_class = 'row_odd';
	$first_letter = '';
	$first_letter_string = '';
	if(isset($data)) foreach ($data as $row_id => $row):
		//$row_class = ($row_class=='row_even') ? 'row_odd' : 'row_even';
		$media_link =  
		$onclick = str_replace(array("\r\n", "\r", "\n", "\t"), ' ', "
$('c". ($column+1) ."').hide();
Effect.Appear('spinner');
new Ajax.Updater('c". ($column+1) ."','". $row['url'] ."', {evalScripts:true});
$$('#c". $column ."in a.row_selected').invoke('removeClassName', 'row_selected');
$('c". $column ."list_". $row_id ."').addClassName('row_selected');
Effect.Fade('spinner');
document.getElementById('scrollto').scrollIntoView();
$('c". $column ."in').scrollTo();
return false;
		");
		if(count($data) > 30) {
			if($first_letter == mb_strtoupper(mb_substr($row['title'], 0, 1, 'UTF-8'))) {
				$first_letter_string = '';
			} else {
				$first_letter = mb_strtoupper(mb_substr($row['title'], 0, 1, 'UTF-8'));
				$first_letter_string = '<a class="row_odd row_header" href="javascript:void(0);">'. $first_letter .'</a>';
			}
		}
		
?>
		<?= $first_letter_string; ?>
		<a id="c<?= $column ?>list_<?= $row_id; ?>" class="<?= $row_class; ?>" href="javascript:void(0);" onclick="<?= $onclick; ?>"><?= $row['title']; ?></a>
<?php endforeach; ?>

</div>

<div id="c<?= ($column+1); ?>"></div>
