function UserProfile() {
  return (
    <div className="flex justify-center items-center h-[100vh] bg-gradient-to-tr from-slate-50 to-blue-100">
      <div className="bg-slate-50 shadow-md rounded-lg p-4">
        <div className="flex justify-center items-center">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            className="w-20 h-20">
            <path
              fillRule="evenodd"
              d="M18.685 19.097A9.723 9.723 0 0 0 21.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 0 0 3.065 7.097A9.716 9.716 0 0 0 12 21.75a9.716 9.716 0 0 0 6.685-2.653Zm-12.54-1.285A7.486 7.486 0 0 1 12 15a7.486 7.486 0 0 1 5.855 2.812A8.224 8.224 0 0 1 12 20.25a8.224 8.224 0 0 1-5.855-2.438ZM15.75 9a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z"
              clipRule="evenodd"
            />
          </svg>
        </div>
        <h1 className="text-xl font-semibold text-black text-center">
          Subrata Mondal
        </h1>
        <div className="p-4 my-4 rounded-md bg-slate-100 shadow-md border-black ">
          <div className="flex justify-start items-center border-b-2 pb-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-6 h-6 mr-2">
              <path d="M1.5 8.67v8.58a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3V8.67l-8.928 5.493a3 3 0 0 1-3.144 0L1.5 8.67Z" />
              <path d="M22.5 6.908V6.75a3 3 0 0 0-3-3h-15a3 3 0 0 0-3 3v.158l9.714 5.978a1.5 1.5 0 0 0 1.572 0L22.5 6.908Z" />
            </svg>
            <p className="m-2">subratasubha2@gmail.com</p>
          </div>
          <p className="border-b-2 py-2">Your Preferences</p>
          <div className="border-b-2 py-2">
            <div className="flex justify-between items-center">
              <div>
                <input
                  id="ml"
                  type="checkbox"
                  className="default:ring-2 mr-2"
                />
                <label htmlFor="ml">ML</label>
              </div>
              <div>
                <input
                  id="cv"
                  type="checkbox"
                  className="default:ring-2 mr-2"
                />
                <label htmlFor="cv">CV</label>
              </div>
              <div>
                <input
                  id="nlp"
                  type="checkbox"
                  className="default:ring-2 mr-2"
                />
                <label htmlFor="nlp">NLP</label>
              </div>
              <div>
                <input
                  id="llm"
                  type="checkbox"
                  className="default:ring-2 mr-2"
                />
                <label htmlFor="llm">LLM</label>
              </div>
            </div>
          </div>
        </div>
        <div className="flex justify-center items-center">
          <button className="px-4 py-2 bg-black text-white font-bold rounded-full">
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
