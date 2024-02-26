import { useState } from "react";
function ExpandableText() {
  const [isClamped, setIsClamped] = useState(true); // Initial state is clamped
  const handleClick = () => {
    setIsClamped(!isClamped); // Toggle on button click
  };

  return (
    <>
      <p className={`${isClamped ? "line-clamp-3" : "lg:line-clamp-none"}`}>
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto
        laborum veniam accusantium cum error magnam nesciunt vel assumenda!
        Necessitatibus, modi illum. Aliquam iure pariatur dolorem error. Est
        nostrum et illo exercitationem harum voluptate, unde expedita ratione
        temporibus repellat, atque error corrupti officia, ullam reprehenderit
        delectus eos. Accusamus ex ea blanditiis! Vero sint iure pariatur rem
        velit distinctio maiores assumenda, incidunt alias explicabo, delectus
        est? Ut qui quis hic modi expedita ipsa, tempora neque cum, aut nesciunt
        excepturi quisquam animi molestias possimus voluptatum, illum magnam.
        Facere eligendi adipisci, nostrum aliquid, beatae voluptatibus ad ab
        deleniti veritatis labore, earum dignissimos. Ad, dolorum!
      </p>
      <button
        onClick={handleClick}
        className="text-2xl font-bold text-blue-600">
        {isClamped ? "+" : "-"}
      </button>
    </>
  );
}
export default ExpandableText;
