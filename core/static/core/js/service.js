function isEmptyInput(input)
{
  return input.value == '';
}

function validateTaskFields()
{
  var title = document.getElementById("id_title");  

  if (isEmptyInput(title) )
  {
    return false;
  }

  return true;
}

function submitAddTask()
{

  if (!validateTaskFields() )
  {
    return;
  }

  var form = document.getElementById("add-task-form-id");
 
  form.submit();

}

function submitDeleteTask(todo_id)
{
  if (confirm("Remove task?")) {

    form_id = `remove-task-${todo_id}-form-id`;

    var form = document.getElementById(form_id);

    form.submit();
  }
}