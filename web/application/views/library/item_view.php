<script type="text/javascript">
	$('c<?= $column; ?>in').setStyle({left:($('c<?= $column; ?>in').up(0).previous(0).positionedOffset().left+$('c<?= $column; ?>in').up(0).previous(0).getWidth()+'px')});
	$('c<?= $column; ?>').show();
</script>
<div id="c<?= $column; ?>in" class="right_frame_column">
<pre>
<?php

	print_r($media);

?>
</pre>
</div>