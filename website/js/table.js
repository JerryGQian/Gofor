$(document).ready(function(){
	$('#table_id').DataTable({dom:'f'});
	$('#table_id_filter input').removeClass('searchClass');
	$('#table_id_filter input').addClass('mySearch');
});

