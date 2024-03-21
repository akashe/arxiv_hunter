import { useState } from "react";

function ExpandableText({ title }) {
  const [isClamped, setIsClamped] = useState(true); // Initial state is clamped
  const handleClick = () => {
    setIsClamped(!isClamped); // Toggle on button click
  };

  return (
    <>
      <p className={`${isClamped ? "line-clamp-3" : "lg:line-clamp-none"}`}>{title}</p>
      <button
        onClick={handleClick}
        className="font-sm text-blue-600">
        {isClamped ? "Read more..." : "...read less"}
      </button>
    </>
  )
}
export default ExpandableText;
