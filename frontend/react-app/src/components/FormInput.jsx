function FormInput(props) {
  return (
    <div className="formInput">
      <input
        ref={props.usernameRef}
        className="p-[15px] my-[10px] mx-0 w-full px-4 py-4 rounded-sm bg-slate-100 text-gray-700 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-100"
        type="text"
        placeholder={props.placheHolder}
      />
    </div>
  );
}

export default FormInput;
