%include <zypp/RepoManager.h>

#ifdef SWIGPYTHON
%extend  zypp::RepoManager{
    std::string loadSolvFile(std::string _solv, std::string _alias)
    {
        RepoInfo tmpRepo; 
        tmpRepo.setAlias(_alias);
        try {
            sat::Pool::instance().addRepoSolv(_solv, tmpRepo);
        } catch ( const Exception & e ){
            return e.msg();
        }

        return std::string();
    }
}
#endif

