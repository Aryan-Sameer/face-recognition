import React from 'react'
import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <div className='w-3/4'>
      <Link to="/">
        <button className="cursor-pointer text-2xl font-bold m-2">{`<`}</button>
      </Link>
    </div>
  )
}

export default Navigation
