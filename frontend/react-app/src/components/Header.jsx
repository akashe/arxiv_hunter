function Header ()
{
    return (
        <header className="fixed top-0 left-0 right-0 z-10 text-slate-800 h-16 bg-white shadow-md flex items-center justify-between px-4">
            <h1 className="text-2xl font-bold">Arxiv Hunter</h1>
            <div className="hidden lg:block flex-grow"></div>
            <button
                className="text-xl font-bold text-slate-800 border-slate-800 text-center bg-slate-200 rounded-full h-10 w-10 mr-2 hover:bg-slate-300">P</button>
        </header>

    )
}

export default Header