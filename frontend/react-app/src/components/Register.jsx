import { useState } from "react";
import { Link } from "react-router-dom";
import Choice from "./Choice";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Validate form data (optional, but recommended)
    if (!username || !password || !password2 || !email) {
      setMessage("Please fill in all required fields.");
      return;
    }

    if (password !== password2) {
      setMessage("Passwords do not match.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
          password2, // Assuming your backend requires password2 for registration
          email,
        }),
      });

      if (!response.ok) {
        setMessage("Registration failed. Please try again.");
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setMessage(data.message || "Registration successful!"); // Handle success message (if applicable)
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred. Please try again later.");
    }
  };
  return (
    <div className="flex justify-center items-center h-[100vh] bg-gradient-to-tr from-slate-50 to-blue-100">
      <form onSubmit={handleSubmit}>
        <div className="bg-slate-50 shadow-md rounded-lg p-4">
          <div className="flex justify-center items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-10 h-10">
              <path d="M11.7 2.805a.75.75 0 0 1 .6 0A60.65 60.65 0 0 1 22.83 8.72a.75.75 0 0 1-.231 1.337 49.948 49.948 0 0 0-9.902 3.912l-.003.002c-.114.06-.227.119-.34.18a.75.75 0 0 1-.707 0A50.88 50.88 0 0 0 7.5 12.173v-.224c0-.131.067-.248.172-.311a54.615 54.615 0 0 1 4.653-2.52.75.75 0 0 0-.65-1.352 56.123 56.123 0 0 0-4.78 2.589 1.858 1.858 0 0 0-.859 1.228 49.803 49.803 0 0 0-4.634-1.527.75.75 0 0 1-.231-1.337A60.653 60.653 0 0 1 11.7 2.805Z" />
              <path d="M13.06 15.473a48.45 48.45 0 0 1 7.666-3.282c.134 1.414.22 2.843.255 4.284a.75.75 0 0 1-.46.711 47.87 47.87 0 0 0-8.105 4.342.75.75 0 0 1-.832 0 47.87 47.87 0 0 0-8.104-4.342.75.75 0 0 1-.461-.71c.035-1.442.121-2.87.255-4.286.921.304 1.83.634 2.726.99v1.27a1.5 1.5 0 0 0-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.66a6.727 6.727 0 0 0 .551-1.607 1.5 1.5 0 0 0 .14-2.67v-.645a48.549 48.549 0 0 1 3.44 1.667 2.25 2.25 0 0 0 2.12 0Z" />
              <path d="M4.462 19.462c.42-.419.753-.89 1-1.395.453.214.902.435 1.347.662a6.742 6.742 0 0 1-1.286 1.794.75.75 0 0 1-1.06-1.06Z" />
            </svg>
          </div>
          <h1 className="text-2xl font-semibold text-black text-center">
            {`Let's create your account`}
          </h1>
          <p className="text-sm text-center text-slate-500">
            Please provide your details
          </p>
          <div className="p-4 my-4 rounded-md bg-slate-100 shadow-md border-black ">
            <div className="flex justify-start items-center pb-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-6 h-6 mx-2 absolute">
                <path
                  fillRule="evenodd"
                  d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
                  clipRule="evenodd"
                />
              </svg>
              <input
                id="username"
                className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
                placeholder="Full Name"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="flex justify-start items-center pb-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-6 h-6 mx-2 absolute">
                <path d="M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z" />
                <path d="M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z" />
              </svg>
              <input
                id="email"
                className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
                placeholder="example@gmail.com"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="flex justify-start items-center pb-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-6 h-6 mx-2 absolute">
                <path
                  fillRule="evenodd"
                  d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z"
                  clipRule="evenodd"
                />
              </svg>
              <input
                id="password1"
                className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="flex justify-start items-center pb-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-6 h-6 mx-2 absolute">
                <path
                  fillRule="evenodd"
                  d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z"
                  clipRule="evenodd"
                />
              </svg>
              <input
                id="password2"
                className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
                placeholder="Confirm Password"
                type="password"
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
                required
              />
            </div>
            <p className="text-sm border-b-2 py-2 text-slate-700">
              Select your preferences
            </p>
            <div className="border-b-2 py-2">
              <div className="flex justify-between items-center">
                <Choice name="ML"></Choice>
                <Choice name="CV"></Choice>
                <Choice name="NLP"></Choice>
                <Choice name="LLM"></Choice>
              </div>
            </div>
            <div>
              <Link to={"/login"}>
                <p className="text-sm text-slate-500 text-center py-2">
                  Already a user? Login instead
                </p>
              </Link>
            </div>
            <div className="flex justify-center items-center">
              <button
                type="submit"
                className="px-4 py-2 bg-black text-white font-bold rounded-full">
                Register
              </button>
            </div>
          </div>
          <div className="text-sm text-slate-500 py-2 text-center">
            {message && <p>{message}</p>}
          </div>
        </div>
      </form>
    </div>
  );
}

export default Register;
