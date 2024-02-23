import { useState } from "react";

function LoginSignup() {
  const [action, setAction] = useState("Sign Up");
  const loginMsg = "Welcome back";
  const signupMsg = "Create account";
  const inputBar =
    "p-4 my-2 rounded-full bg-blue-100 hover:shadow-md font-bold focus:outline-blue-500 focus:ring-2 focus:ring-blue-500";
  const displayFullName = (
    <div className="flex flex-col">
      <input
        type="text"
        placeholder="first name"
        className={inputBar}
      />
      <input
        type="text"
        placeholder="last name"
        className={inputBar}
      />
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
              type="text"
              placeholder="email"
              className={inputBar}
            />
            <input
              type="text"
              placeholder="password"
              className={inputBar}
            />
            {action === "Log In" && loginInfo}
            {action === "Sign Up" && signupInfo}

            <button className="p-4 my-2 rounded-full bg-blue-600 hover:bg-blue-700 hover:shadow-md text-xl  font-bold text-white">
              {action}
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

export default LoginSignup;
