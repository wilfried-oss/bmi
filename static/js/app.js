$(function () {
  const $form = $("#bmi-form");
  const $weight = $("#weight");
  const $height = $("#height");
  const $result = $("#result-card");
  const $error = $("#error-message");
  const $reset = $("#reset-button");
  const $bmiValue = $("#bmi-value");
  const $bmiAdvice = $("#bmi-advice");

  function showError(message) {
    $error.text(message).prop("hidden", false);
  }

  function hideError() {
    $error.text("").prop("hidden", true);
  }

  function displayResult(data) {
    $bmiValue.text(Number(data.bmi));
    $bmiAdvice.text(data.advice);
    $result.prop("hidden", false);
    $form.hide();
  }

  $form.on("submit", function (event) {
    event.preventDefault();
    hideError();

    fetch("/calculate_bmi", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        weight: Number($weight.val()),
        height: Number($height.val()),
      }),
    })
      .then(async (response) => {
        const data = await response.json();
        if (!response.ok) {
          let message = "Unable to calculate BMI. Please try again.";
          if (data.detail) {
            message = Array.isArray(data.detail)
              ? data.detail.map((item) => item.msg).join(", ")
              : data.detail;
          }
          throw new Error(message);
        }
        displayResult(data);
      })
      .catch((err) => {
        showError(err.message);
      });
  });

  $reset.on("click", function () {
    $form[0].reset();
    $result.prop("hidden", true);
    hideError();
    $form.show();
    $weight.focus();
  });
});
