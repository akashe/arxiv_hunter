import FormInput from "../components/FormInput";
function Form() {
  return (
    <div className="app flex justify-center items-center h-[100vh]">
      <form action="">
        <FormInput placheHolder="Username"></FormInput>
        <FormInput placheHolder="First Name"></FormInput>
        <FormInput placheHolder="Last Name"></FormInput>
        <FormInput placheHolder="Email"></FormInput>
      </form>
    </div>
  );
}

export default Form;
