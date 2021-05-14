$("#show-password-checkbox").click(function () {
	let pass_field = $("#id_password");

	if (pass_field.attr("type") === "password") {
		pass_field.attr("type", "text");
	} else {
		pass_field.attr("type", "password");
	}
});
