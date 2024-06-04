import { useState } from "react";

function ExpandableText({ title }) {
  const [isClamped, setIsClamped] = useState(true); // Initial state is clamped
  const handleClick = () => {
    setIsClamped(!isClamped); // Toggle on button click
  };

  return (
    <>
      <div className={`${isClamped ? "line-clamp-3" : "lg:line-clamp-none"}`}>{title}</div>
      <button
        onClick={handleClick}
        className="font-sm text-blue-600">
        {isClamped ? "Read more..." : "...read less"}
      </button>
    </>
  )
}
export default ExpandableText;
