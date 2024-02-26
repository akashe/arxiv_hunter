import { useState } from "react";

function Accordion() {
  const [accordionOpen, setAccordionOpen] = useState(false);
  return (
    <div>
      <div
        className={`grid overflow-hidden transition-all duration-300 ease-out text-slate-600 ${
          accordionOpen
            ? "grid-rows-[1fr] opacity-100"
            : "grid-rows-[0fr] opacity-0"
        }`}>
        This is the answer
      </div>
    </div>
  );
}

export default Accordion;
