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
    $bmiValue.text(Number(data.bmi).toFixed(2));
    $bmiAdvice.text(data.advice);
    $result.prop("hidden", false);
    $form.hide();
  }

  $form.on("submit", function (event) {
    event.preventDefault();
    hideError();
    method: ("POST",
      fetch("/calculate_bmi", {
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
          weight: Number($weight.val()),
          height: Number($height.val()),
        }),
      })
        .then(async (response) => {
          const data = await response.json();

          if (!response.ok) {
            const message = Array.isArray(data.detail)
              ? data.detail
                  .map((item) => {
                    const field = item.loc[item.loc.length - 1];
                    return `${field}: ${item.msg}`;
                  })
                  .join(", ")
              : data.detail || "Unable to calculate BMI. Please try again.";
            throw new Error(message);
          }

          displayResult(data);
        })
        .catch((error) => {
          showError(error.message);
        }));
  });

  $reset.on("click", function () {
    $form[0].reset();
    $result.prop("hidden", true);
    hideError();
    $form.show();
    $weight.focus();
  });
});
