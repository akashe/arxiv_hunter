function Header ()
{
    return (
        <header className="fixed top-0 left-0 right-0 z-10 text-slate-800 h-16 bg-white shadow-md flex items-center justify-between px-4">
            <h1 className="text-2xl font-bold">Arxiv Hunter</h1>
            <div className="hidden lg:block flex-grow"></div>
            <button
                className="text-xl font-bold text-slate-800 border-slate-800 text-center bg-slate-200 rounded-full h-10 w-10 mr-2 hover:bg-slate-300 flex justify-center items-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                </button>
        </header>

    )
}

export default Header