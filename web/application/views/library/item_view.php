<script type="text/javascript">
	$('c<?= $column; ?>in').setStyle({left:($('c<?= $column; ?>in').up(0).previous(0).positionedOffset().left+$('c<?= $column; ?>in').up(0).previous(0).getWidth()+'px')});
	$('c<?= $column; ?>').show();
</script>
<div id="c<?= $column; ?>in" class="right_frame_column" style="border:none; max-width:1500px;">

<?php	if(isset($media)) foreach ($media as $media_id => $media_value): ?>

	<h2><?= $media_value['title'] ?></h2>

		<table class="vertical_table" cellspacing="0" cellpadding="0">
		<?php if(isset($media_value['tags'])) foreach ($media_value['tags'] as $tag_id => $tag_value): if(is_array($tag_value)) { ?>
			<tr valign="top">
				<th><?= $this->lang1->str($tag_id) ?>:</th>
				<td>
					<?= $this->arxui->tag_links($tag_id, $tag_value) ?>
				</td>
			</tr>
		<?php } endforeach; ?>
		</table>
	
	<h2><?= $this->lang1->str('Items') ?></h2>

		<table class="horisontal_table" cellspacing="0" cellpadding="0" style="width:400px;">
			<tr valign="top">
				<th><?= $this->lang1->str('item_number') ?></th>
				<th><?= $this->lang1->str('barcode') ?></th>
				<th><?= $this->lang1->str('quantity') ?></th>
				<th><?= $this->lang1->str('price') ?></th>
				<th style="border-right:none;"><?= $this->lang1->str('note') ?></th>
			</tr>
		<?php if(isset($media_value['items'])) foreach ($media_value['items'] as $item_id => $item_value): ?>
			<tr valign="top">
				<td style="text-align:right;"><?= rtrim(rtrim($item_value['item_number'], '0'), '.') ?>&nbsp;</td>
				<td style="text-align:center;"><?= $item_value['barcode'] ?>&nbsp;</td>
				<td style="text-align:center;"><?= $item_value['quantity'] ?>&nbsp;</td>
				<td style="text-align:right;"><?= $item_value['price'] ?>&nbsp;</td>
				<td style="border-right:none;"><?= $item_value['note'] ?>&nbsp;</td>
			</tr>
		<?php endforeach; ?>
		</table>

	<h2><?= $this->lang1->str('Notes') ?></h2>
	<p class="text"><?= $media_value['note'] ?></p>

<?php endforeach; ?>

<pre>
<?php

	//print_r($media);

?>
</pre>
</div>
