def signupModal():
    return ('''
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title" id="exampleModalLabel">Signup</h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <form>
            <div class="form-group">
                <label for="recipient-name" class="col-form-label">Userid</label>
                <input type="text" class="form-control" id="recipient-name">
            </div>
            <div class="form-group">
                <label for="email" class="col-form-label">Email</label>
                <input type="email" name="email" id="email"  class="form-control">
            </div>
            <div class="form-group">
                <label for="password" class="col-form-label">Password</label>
                <input type="password" name="password" id="password"  class="form-control">
            </div>
            </form>
        </div>
        <div class="modal-footer">
            <a href="#" data-toggle="modal" data-target="#loginModal" data-whatever="@getbootstrap">Existing user? Log in</a>

            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary">Register</button>
        </div>
        </div>
    </div>
    </div>
    ''')

def loginModal():
    return ('''
        <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header"  style="padding:30px 10px">
            <h4 class="modal-title" id="exampleModalLabel">Signup</h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body"   style="padding:30px 10px">
            <form>
            <div class="form-group">
                <label for="email" class="col-form-label">Email</label>
                <input type="email" name="email" id="email"  class="form-control">
            </div>
            <div class="form-group">
                <label for="password" class="col-form-label">Password</label>
                <input type="password" name="password" id="password"  class="form-control">
            </div>
            </form>
        </div>
        <div class="modal-footer" style="padding:30px 10px">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary">Login</button>
        </div>
        </div>
    </div>
    </div>
    ''')