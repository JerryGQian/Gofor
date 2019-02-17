$(document).ready(function(){
	table = $('#table_id').DataTable({dom:'fl'});
	table1 = $('#table_id1').DataTable({dom:'f'});
	$('#table_id_filter input').removeClass('searchClass');
	$('#table_id_filter input').addClass('mySearch');

	$('#table_id tbody').on('click', 'tr', function () {
		$('#news div').hide();
        var data = table.row( this ).data();
        var comp_div = $('#'+data);
        comp_div.show();
    } );
});

