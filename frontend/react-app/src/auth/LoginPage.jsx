import { useRef, useState, useEffect } from "react"
import { Link, useNavigate, useLocation } from "react-router-dom"

import axios from "../api/api"
import "./LoginPage.css"

const LOGIN_URL = "/login"

const LoginPage = () => {
  const navigate = useNavigate()
  const location = useLocation()
  const from = location.state?.from?.pathname || "/"

  const userRef = useRef()
  const errRef = useRef()

  const [user, setUser] = useState("")
  const [pwd, setPwd] = useState("")
  const [errMsg, setErrMsg] = useState("")

  useEffect(() => {
    userRef.current.focus()
  }, [])

  useEffect(() => {
    setErrMsg("")
  }, [user, pwd])

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await axios.post(LOGIN_URL, JSON.stringify({ username: user, password: pwd }), {
        headers: { "Content-Type": "application/json" },
        withCredentials: true,
      })
      localStorage.setItem("appToken", response.data.token)
      localStorage.setItem("userEmail", response.data.username)
      console.log(localStorage.getItem("appToken"))
      console.log(JSON.stringify(response?.data))

      setUser("")
      setPwd("")
      navigate("/", { replace: true })
    } catch (err) {
      console.log(err) // Log the entire error object
      if (!err.response) {
        setErrMsg("No Server Response")
      } else if (err.response.status === 400) {
        setErrMsg("Missing Username or Password")
      } else if (err.response.status === 401) {
        setErrMsg("Unauthorized")
      } else {
        setErrMsg("Login Failed")
      }
      errRef.current.focus()
    }
  }

  return (
    <div className="flex justify-center items-center h-[100vh] bg-gradient-to-tr from-slate-50 to-blue-100">
      <div className="border-2 bg-white border-gray-200 p-10 rounded-lg shadow-md">
        <section id="login-section">
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive">
            {errMsg}
          </p>
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
          <h1 className="text-2xl font-semibold text-black text-center">{`Welcome Back`}</h1>
          <p className="text-sm text-center text-slate-500">Please provide your details</p>
          <form
            onSubmit={handleSubmit}
            className="login-form">
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
              className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
            />

            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
              className="px-10 py-2 rounded-full bg-slate-200 text-gray-600 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-opacity-60"
            />
            <button className="px-4 py-2 bg-black text-white font-bold rounded-full">Sign In</button>
          </form>
          <div>
            <Link to={"/register"}>
              <p className="text-sm font-bold text-blue-500 text-center pb-2">New user? Register instead</p>
            </Link>
          </div>
        </section>
      </div>
    </div>
  )
}

export default LoginPage
