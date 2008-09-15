<div id="tagvalues" class="right_frame_column" style="width:200px;left:121px;">

<?php 
	$row_class = 'table_row_odd';
	if(isset($tagvalues)) foreach ($tagvalues as $tagvalue_id => $tagvalue):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
		$media_link =  site_url('library/search/'. rawurlencode(serialize(array('type'=>'all','search'=>array(array('tagtype'=>$tagvalue['tagtype'],'operator'=>'is','value'=>$tagvalue['value']))))) .'/1/true');
		$onclick = "
Effect.Appear('spinner');
new Ajax.Updater('col3','". $media_link ."');
$$('#tagvalues a.column_row').invoke('removeClassName', 'table_row_selected');
$('tagvalue_". $tagvalue_id ."').addClassName('table_row_selected');
Effect.Fade('spinner');
return false;
		";
?>
		<a id="tagvalue_<?= $tagvalue_id; ?>" class="black_a column_row <?= $row_class; ?>" href="javascript:void(0);" onclick="<?= $onclick; ?>"><?= $tagvalue['value'] ?></a>

<?php endforeach; ?>

</div>

<div id="col3" class="right_frame_column" style="width:400px;left:322px;"></div>
