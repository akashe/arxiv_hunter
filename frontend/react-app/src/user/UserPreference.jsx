import { useState } from "react"
import { toast } from "react-toastify"

const UserPreference = () => {
  const [userInput, setUserInput] = useState("")
  const [isIconClicked, setIsIconClicked] = useState(false)

  const handleInputChange = (event) => {
    setUserInput(event.target.value)
  }

  const handleIconClick = () => {
    setIsIconClicked(true)
    const preferences = localStorage.getItem("preferences")
    if (preferences) {
      toast(`Your preferences are: ${preferences}, ${userInput}`)
    } else {
      toast(`Your preferences are: ${userInput}`)
    }
  }

  return (
    <div className="flex flex-col">
      <p className="pt-1">Your Custom preferences</p>
      {isIconClicked && <p className="text-slate-500 line-clamp-3">{userInput}</p>}
      {/* <label
        className="py-2 text-black text-base"
        htmlFor="username">
        Add custom preferences
      </label> */}
      <div className="relative flex items-center w-[250px]">
        <input
          type="text"
          id="username"
          autoComplete="off"
          required
          value={userInput}
          onChange={handleInputChange}
          className="px-4 my-2 w-[230px] bg-transparent py-2 rounded-full border-2 border-slate-500 text-gray-600 focus:outline-none"
          placeholder="Add custom preferences"
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="w-6 h-6 absolute right-7 top-1/2 transform -translate-y-1/2 cursor-pointer"
          onClick={handleIconClick}>
          <path
            fillRule="evenodd"
            d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z"
            clipRule="evenodd"
          />
        </svg>
      </div>
    </div>
  )
}

export default UserPreference
