function Footer ()
{
    return <footer className="fixed bottom-0 left-0 right-0 z-10 h-16 bg-white flex items-center justify-center">
        <div className="relative flex items-center w-full max-w-[800px]">
            <input type="text" className="w-full px-4 py-2 rounded-full bg-slate-300 text-gray-700 focus:outline-none focus:ring-2 focus:ring-slate-800 focus:ring-opacity-60" placeholder="Search here..."/>
            <img src="logo.svg" alt="Logo" className="absolute right-4 top-1/2 transform -translate-y-1/2 h-6 w-6"/>
        </div>

    </footer>
}

export default Footer