const UserPreference = () => {
  return (
    <div className="flex flex-col">
      <label
        className="py-2 text-black text-base"
        htmlFor="username">
        Add custom preferences
      </label>
      <input
        type="text"
        id="username"
        autoComplete="off"
        required
        className="px-10 bg-transparent py-2 rounded-full border-2 border-slate-500 text-gray-600 focus:outline-none "
      />
    </div>
  )
}

export default UserPreference
