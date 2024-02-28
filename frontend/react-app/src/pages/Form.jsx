import FormInput from "../components/FormInput";
import { useState, useRef } from "react";

function Form() {
  // const [username, setUsername] = useState("");
  const usernameRef = useRef();
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(usernameRef);
  };
  return (
    <div className="app flex justify-center items-center h-[100vh]">
      <form
        action=""
        onSubmit={handleSubmit}>
        <FormInput
          refer={usernameRef}
          placheHolder="Username"></FormInput>
        <FormInput placheHolder="First Name"></FormInput>
        <FormInput placheHolder="Last Name"></FormInput>
        <FormInput placheHolder="Email"></FormInput>
        <button>Submit</button>
      </form>
    </div>
  );
}

export default Form;
