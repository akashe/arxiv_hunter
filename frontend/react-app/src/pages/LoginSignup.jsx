import { useState } from "react";
import { useForm } from "react-hook-form";

function LoginSignup() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => {
    console.log(data);
  };
  const [action, setAction] = useState("Sign Up");
  const loginMsg = "Welcome back";
  const signupMsg = "Create account";
  const inputBar =
    "p-4 my-2 rounded-full bg-blue-100 hover:shadow-md font-bold focus:outline-blue-500 focus:ring-2 focus:ring-blue-500";
  const displayFullName = (
    <div className="flex flex-col">
      <input
        {...register("firstname", {
          required: "Firstname is required, length > 2",
          minLength: 3,
        })}
        type="text"
        placeholder="first name"
        className={inputBar}
      />
      {errors.firstname && (
        <div className="text-red-500">{errors.firstname.message}</div>
      )}
      <input
        {...register("lastname", {
          required: "Lastname is required, length > 2",
          minLength: 3,
        })}
        type="text"
        placeholder="last name"
        className={inputBar}
      />
      {errors.lastname && (
        <div className="text-red-500">{errors.lastname.message}</div>
      )}
    </div>
  );
  const loginInfo = (
    <div className="flex justify-between">
      <button
        onClick={() => setAction("Sign Up")}
        className="text-slate-600 hover:text-slate-900">
        New User?
      </button>
      <button className="text-slate-500 hover:text-slate-900">
        Forgot Password?
      </button>
    </div>
  );

  const signupInfo = (
    <button
      onClick={() => setAction("Log In")}
      className="text-slate-600 hover:text-slate-900">
      Existing User?
    </button>
  );

  return (
    <section className="min-h-screen flex justify-center items-center bg-gradient-to-tr from-white to-blue-200">
      <form
        action=""
        onSubmit={handleSubmit(onSubmit)}>
        <div className="w-full m-8 rounded-lg shadow-md max-w-[600px]">
          <div className="m-4">
            <div className="flex flex-col">
              <div className="text-center mb-8">
                <h1 className="text-5xl">
                  {action === "Log In" && loginMsg}
                  {action === "Sign Up" && signupMsg}
                </h1>
                <p className="font-semibold mt-2">Please enter your details</p>
              </div>
              {action === "Sign Up" && displayFullName}
              <input
                {...register("email", {
                  required: "Email is required, length > 2",
                  minLength: 3,
                  validate: (value) => value.includes("@"),
                })}
                type="text"
                placeholder="email"
                className={inputBar}
              />
              {errors.email && (
                <div className="text-red-500">{errors.email.message}</div>
              )}
              <input
                {...register("password", {
                  required: "Password is required, length > 7",
                  minLength: 8,
                })}
                type="text"
                placeholder="password"
                className={inputBar}
              />
              {errors.password && (
                <div className="text-red-500">{errors.password.message}</div>
              )}
              {action === "Log In" && loginInfo}
              {action === "Sign Up" && signupInfo}

              <button className="p-4 my-2 rounded-full bg-blue-600 hover:bg-blue-700 hover:shadow-md text-xl  font-bold text-white">
                {action}
              </button>
            </div>
          </div>
        </div>
      </form>
    </section>
  );
}

export default LoginSignup;
