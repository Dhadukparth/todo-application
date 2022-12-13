$(document).ready( function () {
    $('#myTable').DataTable();

    
} );
$('.editTodoBtn').on('click', function () {
    let todoid = $(this).attr('data-id');

    $.ajax({
        type: "GET",
        url: "/editTodo/",
        data: {
            'todo_id':todoid
        },
        success: function (res) {
            $('#editTodoModal').modal('show');
            $('#editodo_id').val(res.todo_id);
            $('#editodo_name').val(res.todo_name);
            $('#editodo_description').val(res.todo_description);
        }
    });
});
