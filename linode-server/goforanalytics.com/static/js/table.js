$(document).ready(function(){
	table = $('#table_id').DataTable({
		dom: 'fp',
		columns: [
			{name: 'symbol'},
			{name: 'date'},
			{name: 'low'},
			{name: 'high'},
			{name: 'close'},
		],
		ajax : {
			url : 'http://services.goforanalytics.com/predictions',
			type: 'get',
		}
	});
	table1 = $('#news_table').DataTable({dom:'f'});
	$('#table_id_filter input').removeClass('searchClass');
	$('#table_id_filter input').addClass('mySearch');
	$('#news_table_filter input').removeClass('searchClass');
	$('#tnews_table_filter input').addClass('mySearch');

	$('#table_id tbody').on('click', 'tr', function () {
		$('#news div').hide();
        var data = table.row( this ).data();
        var comp_div = $('#'+data[0]);
        comp_div.show();
        $('#wrap').show();
    } );
});

