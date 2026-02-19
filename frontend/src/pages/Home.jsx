import React from 'react'
import FaceVerification from "../components/FaceVerification"

const Home = () => {
    return (
        <div className='w-3/4'>
            <h1 className="text-5xl text-center font-extrabold my-4">Buddy Robot On-Campus</h1>
            <FaceVerification />
        </div>
    )
}

export default Home
