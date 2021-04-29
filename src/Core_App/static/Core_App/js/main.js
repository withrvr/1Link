let user_profile_picture = document.getElementById("user_profile_picture");
if (user_profile_picture) {
	user_profile_picture.style.height = `${user_profile_picture.offsetWidth}px`;

	window.addEventListener("resize", function (e) {
		user_profile_picture.style.height = `${user_profile_picture.offsetWidth}px`;
	});
}
