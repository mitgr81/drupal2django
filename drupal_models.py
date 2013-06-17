'''Copyright (c) 2010-2012 Jared Forsyth

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Access(Base):
    __tablename__ = u'access'
    aid = Column(Integer, primary_key=True)
    mask = Column(String(765))
    type = Column(String(765))
    status = Column(Integer)


class Accesslog(Base):
    __tablename__ = u'accesslog'
    aid = Column(Integer, primary_key=True)
    sid = Column(String(192))
    title = Column(String(765))
    path = Column(String(765))
    url = Column(String(765))
    hostname = Column(String(384))
    uid = Column(Integer)
    timer = Column(Integer)
    timestamp = Column(Integer)


class Actions(Base):
    __tablename__ = u'actions'
    aid = Column(String(765), primary_key=True)
    type = Column(String(96))
    callback = Column(String(765))
    parameters = Column(String)
    description = Column(String(765))


class ActionsAid(Base):
    __tablename__ = u'actions_aid'
    aid = Column(Integer, primary_key=True)


class AdvancedHelpIndex(Base):
    __tablename__ = u'advanced_help_index'
    sid = Column(Integer, primary_key=True)
    module = Column(String(765))
    topic = Column(String(765))
    language = Column(String(36))


class AggregatorCategory(Base):
    __tablename__ = u'aggregator_category'
    cid = Column(Integer, primary_key=True)
    title = Column(String(765))
    description = Column(String)
    block = Column(Integer)


class AggregatorCategoryFeed(Base):
    __tablename__ = u'aggregator_category_feed'
    fid = Column(Integer)
    cid = Column(Integer, primary_key=True)


class AggregatorCategoryItem(Base):
    __tablename__ = u'aggregator_category_item'
    iid = Column(Integer)
    cid = Column(Integer, primary_key=True)


class AggregatorFeed(Base):
    __tablename__ = u'aggregator_feed'
    fid = Column(Integer, primary_key=True)
    title = Column(String(765))
    url = Column(String(765))
    refresh = Column(Integer)
    checked = Column(Integer)
    link = Column(String(765))
    description = Column(String)
    image = Column(String)
    etag = Column(String(765))
    modified = Column(Integer)
    block = Column(Integer)


class AggregatorItem(Base):
    __tablename__ = u'aggregator_item'
    iid = Column(Integer, primary_key=True)
    fid = Column(Integer)
    title = Column(String(765))
    link = Column(String(765))
    author = Column(String(765))
    description = Column(String)
    timestamp = Column(Integer)
    guid = Column(String(765))


class Authmap(Base):
    __tablename__ = u'authmap'
    aid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    authname = Column(String(384))
    module = Column(String(384))


class Batch(Base):
    __tablename__ = u'batch'
    bid = Column(Integer, primary_key=True)
    token = Column(String(192))
    timestamp = Column(Integer)
    batch = Column(String)


class Blocks(Base):
    __tablename__ = u'blocks'
    bid = Column(Integer, primary_key=True)
    module = Column(String(192))
    delta = Column(String(96))
    theme = Column(String(192))
    status = Column(Integer)
    weight = Column(Integer)
    region = Column(String(192))
    custom = Column(Integer)
    throttle = Column(Integer)
    visibility = Column(Integer)
    pages = Column(String)
    title = Column(String(192))
    cache = Column(Integer)


class BlocksRoles(Base):
    __tablename__ = u'blocks_roles'
    module = Column(String(192), primary_key=True)
    delta = Column(String(96), primary_key=True)
    rid = Column(Integer)


class BlogapiFiles(Base):
    __tablename__ = u'blogapi_files'
    fid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    filepath = Column(String(765))
    filesize = Column(Integer)


class Boxes(Base):
    __tablename__ = u'boxes'
    bid = Column(Integer, primary_key=True)
    body = Column(String)
    info = Column(String(384))
    format = Column(Integer)


class Cache(Base):
    __tablename__ = u'cache'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheAdminMenu(Base):
    __tablename__ = u'cache_admin_menu'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheBlock(Base):
    __tablename__ = u'cache_block'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheContent(Base):
    __tablename__ = u'cache_content'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheFilter(Base):
    __tablename__ = u'cache_filter'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheForm(Base):
    __tablename__ = u'cache_form'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheMenu(Base):
    __tablename__ = u'cache_menu'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CachePage(Base):
    __tablename__ = u'cache_page'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheUpdate(Base):
    __tablename__ = u'cache_update'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class CacheViews(Base):
    __tablename__ = u'cache_views'
    cid = Column(String(765), primary_key=True)
    data = Column(String)
    expire = Column(Integer)
    created = Column(Integer)
    headers = Column(String)
    serialized = Column(Integer)


class Comments(Base):
    __tablename__ = u'comments'
    cid = Column(Integer, primary_key=True)
    pid = Column(Integer)
    nid = Column(Integer)
    uid = Column(Integer)
    subject = Column(String(192))
    comment = Column(String)
    hostname = Column(String(384))
    timestamp = Column(Integer)
    status = Column(Integer)
    format = Column(Integer)
    thread = Column(String(765))
    name = Column(String(180))
    mail = Column(String(192))
    homepage = Column(String(765))


class Contact(Base):
    __tablename__ = u'contact'
    cid = Column(Integer, primary_key=True)
    category = Column(String(765))
    recipients = Column(String)
    reply = Column(String)
    weight = Column(Integer)
    selected = Column(Integer)


class ContentNodeField(Base):
    __tablename__ = u'content_node_field'
    field_name = Column(String(96), primary_key=True)
    type = Column(String(381))
    global_settings = Column(String)
    required = Column(Integer)
    multiple = Column(Integer)
    db_storage = Column(Integer)
    module = Column(String(381))
    db_columns = Column(String)
    active = Column(Integer)
    locked = Column(Integer)


class ContentNodeFieldInstance(Base):
    __tablename__ = u'content_node_field_instance'
    field_name = Column(String(96), primary_key=True)
    type_name = Column(String(96), primary_key=True)
    weight = Column(Integer)
    label = Column(String(765))
    widget_type = Column(String(96))
    widget_settings = Column(String)
    display_settings = Column(String)
    description = Column(String)
    widget_module = Column(String(381))
    widget_active = Column(Integer)


class ContentTypeProject(Base):
    __tablename__ = u'content_type_project'
    vid = Column(Integer, primary_key=True)
    nid = Column(Integer)
    field_link_url = Column(String(765))
    field_link_title = Column(String(765))
    field_link_attributes = Column(String)
    field_source_url = Column(String(765))
    field_source_title = Column(String(765))
    field_source_attributes = Column(String)


class DevelQueries(Base):
    __tablename__ = u'devel_queries'
    qid = Column(Integer)
    function = Column(String(765))
    query = Column(String)
    hash = Column(String(765), primary_key=True)


class DevelTimes(Base):
    __tablename__ = u'devel_times'
    tid = Column(Integer, primary_key=True)
    qid = Column(Integer)
    time = Column(Float)


class Feedburner(Base):
    __tablename__ = u'feedburner'
    path = Column(String(384), primary_key=True)
    feedburner = Column(String(300))


class Files(Base):
    __tablename__ = u'files'
    fid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    filename = Column(String(765))
    filepath = Column(String(765))
    filemime = Column(String(765))
    filesize = Column(Integer)
    status = Column(Integer)
    timestamp = Column(Integer)


class FilterFormats(Base):
    __tablename__ = u'filter_formats'
    format = Column(Integer, primary_key=True)
    name = Column(String(765))
    roles = Column(String(765))
    cache = Column(Integer)


class Filters(Base):
    __tablename__ = u'filters'
    fid = Column(Integer, primary_key=True)
    format = Column(Integer)
    module = Column(String(192))
    delta = Column(Integer)
    weight = Column(Integer)


class Flood(Base):
    __tablename__ = u'flood'
    fid = Column(Integer, primary_key=True)
    event = Column(String(192))
    hostname = Column(String(384))
    timestamp = Column(Integer)


class History(Base):
    __tablename__ = u'history'
    uid = Column(Integer, primary_key=True)
    nid = Column(Integer)
    timestamp = Column(Integer)


class Image(Base):
    __tablename__ = u'image'
    nid = Column(Integer, primary_key=True)
    fid = Column(Integer)
    image_size = Column(String(96))


class ImageAttach(Base):
    __tablename__ = u'image_attach'
    nid = Column(Integer, primary_key=True)
    iid = Column(Integer)


class Languages(Base):
    __tablename__ = u'languages'
    language = Column(String(36), primary_key=True)
    name = Column(String(192))
    native = Column(String(192))
    direction = Column(Integer)
    enabled = Column(Integer)
    plurals = Column(Integer)
    formula = Column(String(384))
    domain = Column(String(384))
    prefix = Column(String(384))
    weight = Column(Integer)
    javascript = Column(String(96))


class LocalesSource(Base):
    __tablename__ = u'locales_source'
    lid = Column(Integer, primary_key=True)
    location = Column(String(765))
    textgroup = Column(String(765))
    source = Column(String)
    version = Column(String(60))


class LocalesTarget(Base):
    __tablename__ = u'locales_target'
    lid = Column(Integer)
    translation = Column(String)
    language = Column(String(36), primary_key=True)
    plid = Column(Integer)
    plural = Column(Integer)


class MenuCustom(Base):
    __tablename__ = u'menu_custom'
    menu_name = Column(String(96), primary_key=True)
    title = Column(String(765))
    description = Column(String)


class MenuLinks(Base):
    __tablename__ = u'menu_links'
    menu_name = Column(String(96))
    mlid = Column(Integer, primary_key=True)
    plid = Column(Integer)
    link_path = Column(String(765))
    router_path = Column(String(765))
    link_title = Column(String(765))
    options = Column(String)
    module = Column(String(765))
    hidden = Column(Integer)
    external = Column(Integer)
    has_children = Column(Integer)
    expanded = Column(Integer)
    weight = Column(Integer)
    depth = Column(Integer)
    customized = Column(Integer)
    p1 = Column(Integer)
    p2 = Column(Integer)
    p3 = Column(Integer)
    p4 = Column(Integer)
    p5 = Column(Integer)
    p6 = Column(Integer)
    p7 = Column(Integer)
    p8 = Column(Integer)
    p9 = Column(Integer)
    updated = Column(Integer)


class MenuRouter(Base):
    __tablename__ = u'menu_router'
    path = Column(String(765), primary_key=True)
    load_functions = Column(String(765))
    to_arg_functions = Column(String(765))
    access_callback = Column(String(765))
    access_arguments = Column(String)
    page_callback = Column(String(765))
    page_arguments = Column(String)
    fit = Column(Integer)
    number_parts = Column(Integer)
    tab_parent = Column(String(765))
    tab_root = Column(String(765))
    title = Column(String(765))
    title_callback = Column(String(765))
    title_arguments = Column(String(765))
    type = Column(Integer)
    block_callback = Column(String(765))
    description = Column(String)
    position = Column(String(765))
    weight = Column(Integer)
    file = Column(String)


class Node(Base):
    __tablename__ = u'node'
    nid = Column(Integer, primary_key=True)
    vid = Column(Integer, unique=True)
    type = Column(String(96))
    language = Column(String(36))
    title = Column(String(765))
    uid = Column(Integer)
    status = Column(Integer)
    created = Column(Integer)
    changed = Column(Integer)
    comment = Column(Integer)
    promote = Column(Integer)
    moderate = Column(Integer)
    sticky = Column(Integer)
    tnid = Column(Integer)
    translate = Column(Integer)

    def __repr__(self):
        return self.title


class NodeAccess(Base):
    __tablename__ = u'node_access'
    nid = Column(Integer, primary_key=True)
    gid = Column(Integer, primary_key=True)
    realm = Column(String(765), primary_key=True)
    grant_view = Column(Integer)
    grant_update = Column(Integer)
    grant_delete = Column(Integer)


class NodeCommentStatistics(Base):
    __tablename__ = u'node_comment_statistics'
    nid = Column(Integer, primary_key=True)
    last_comment_timestamp = Column(Integer)
    last_comment_name = Column(String(180))
    last_comment_uid = Column(Integer)
    comment_count = Column(Integer)


class NodeCounter(Base):
    __tablename__ = u'node_counter'
    nid = Column(Integer, primary_key=True)
    totalcount = Column(Integer)
    daycount = Column(Integer)
    timestamp = Column(Integer)


class NodeRevisions(Base):
    __tablename__ = u'node_revisions'
    nid = Column(Integer)
    vid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    title = Column(String(765))
    body = Column(String)
    teaser = Column(String)
    log = Column(String)
    timestamp = Column(Integer)
    format = Column(Integer)


class NodeType(Base):
    __tablename__ = u'node_type'
    type = Column(String(96), primary_key=True)
    name = Column(String(765))
    module = Column(String(765))
    description = Column(String)
    help = Column(String)
    has_title = Column(Integer)
    title_label = Column(String(765))
    has_body = Column(Integer)
    body_label = Column(String(765))
    min_word_count = Column(Integer)
    custom = Column(Integer)
    modified = Column(Integer)
    locked = Column(Integer)
    orig_type = Column(String(765))


class NodewordsAttributes(Base):
    __tablename__ = u'nodewords_attributes'
    attid = Column(Integer, primary_key=True)
    tagid = Column(Integer)
    name = Column(String(96))
    value = Column(String(384))
    weight = Column(Integer)


class NodewordsContentNode(Base):
    __tablename__ = u'nodewords_content_node'
    tagid = Column(Integer, primary_key=True)
    nid = Column(Integer)
    vid = Column(Integer, primary_key=True)
    delta = Column(Integer)
    value = Column(String)


class NodewordsDefaults(Base):
    __tablename__ = u'nodewords_defaults'
    tagid = Column(Integer, primary_key=True)
    context = Column(String(192), primary_key=True)
    value = Column(String)
    enabled = Column(Integer)
    editable = Column(Integer)


class NodewordsTags(Base):
    __tablename__ = u'nodewords_tags'
    tagid = Column(Integer, primary_key=True)
    type = Column(String(48))
    name = Column(String(96))
    description = Column(String(384))
    widget = Column(String(48))
    widget_options = Column(String)
    options = Column(String)
    weight = Column(Integer)


class PageTitle(Base):
    __tablename__ = u'page_title'
    nid = Column(Integer, primary_key=True)
    page_title = Column(String(765))


class Permission(Base):
    __tablename__ = u'permission'
    pid = Column(Integer, primary_key=True)
    rid = Column(Integer)
    perm = Column(String)
    tid = Column(Integer)


class PluginManagerQueue(Base):
    __tablename__ = u'plugin_manager_queue'
    short_name = Column(String(765), primary_key=True)


class PluginManagerRepository(Base):
    __tablename__ = u'plugin_manager_repository'
    title = Column(String(765))
    short_name = Column(String(765), primary_key=True)
    links = Column(String(765))


class PluginManagerTaxonomy(Base):
    __tablename__ = u'plugin_manager_taxonomy'
    short_name = Column(String(765), primary_key=True)
    tag = Column(String(765), primary_key=True)


class Role(Base):
    __tablename__ = u'role'
    rid = Column(Integer, primary_key=True)
    name = Column(String(192))


class SearchDataset(Base):
    __tablename__ = u'search_dataset'
    sid = Column(Integer, unique=True, primary_key=True)
    type = Column(String(48))
    data = Column(String)
    reindex = Column(Integer)


class SearchIndex(Base):
    __tablename__ = u'search_index'
    sid = Column(Integer, primary_key=True)
    word = Column(String(150))
    type = Column(String(48))
    score = Column(Float)


class SearchNodeLinks(Base):
    __tablename__ = u'search_node_links'
    sid = Column(Integer, primary_key=True)
    type = Column(String(48), primary_key=True)
    nid = Column(Integer)
    caption = Column(String)


class SearchTotal(Base):
    __tablename__ = u'search_total'
    word = Column(String(150), primary_key=True)
    count = Column(Float)


class Sessions(Base):
    __tablename__ = u'sessions'
    uid = Column(Integer)
    sid = Column(String(192), primary_key=True)
    hostname = Column(String(384))
    timestamp = Column(Integer)
    cache = Column(Integer)
    session = Column(String)


class System(Base):
    __tablename__ = u'system'
    filename = Column(String(765), primary_key=True)
    name = Column(String(765))
    type = Column(String(765))
    owner = Column(String(765))
    status = Column(Integer)
    throttle = Column(Integer)
    bootstrap = Column(Integer)
    schema_version = Column(Integer)
    weight = Column(Integer)
    info = Column(String)


class TermData(Base):
    __tablename__ = u'term_data'
    tid = Column(Integer, primary_key=True)
    vid = Column(Integer)
    name = Column(String(765))
    description = Column(String)
    weight = Column(Integer)


class TermHierarchy(Base):
    __tablename__ = u'term_hierarchy'
    tid = Column(Integer, primary_key=True)
    parent = Column(Integer)


class TermNode(Base):
    __tablename__ = u'term_node'
    nid = Column(Integer)
    vid = Column(Integer)
    tid = Column(Integer, primary_key=True)


class TermRelation(Base):
    __tablename__ = u'term_relation'
    trid = Column(Integer, primary_key=True)
    tid1 = Column(Integer, unique=True)
    tid2 = Column(Integer)


class TermSynonym(Base):
    __tablename__ = u'term_synonym'
    tsid = Column(Integer, primary_key=True)
    tid = Column(Integer)
    name = Column(String(765))


class TinymceRole(Base):
    __tablename__ = u'tinymce_role'
    name = Column(String(384), primary_key=True)
    rid = Column(Integer, primary_key=True)


class TinymceSettings(Base):
    __tablename__ = u'tinymce_settings'
    name = Column(String(384), primary_key=True)
    settings = Column(String)


class Upload(Base):
    __tablename__ = u'upload'
    fid = Column(Integer)
    nid = Column(Integer)
    vid = Column(Integer, primary_key=True)
    description = Column(String(765))
    list = Column(Integer)
    weight = Column(Integer)


class UrlAlias(Base):
    __tablename__ = u'url_alias'
    pid = Column(Integer, primary_key=True)
    src = Column(String(384))
    dst = Column(String(384))
    language = Column(String(36))


class Users(Base):
    __tablename__ = u'users'
    uid = Column(Integer, primary_key=True)
    name = Column(String(180))
    pass_field = Column('pass', String(96))  # Field renamed because it was a Python reserved word. Field name made lowercase.
    mail = Column(String(192))
    mode = Column(Integer)
    sort = Column(Integer)
    threshold = Column(Integer)
    theme = Column(String(765))
    signature = Column(String(765))
    created = Column(Integer)
    access = Column(Integer)
    login = Column(Integer)
    status = Column(Integer)
    timezone = Column(String(24))
    language = Column(String(36))
    picture = Column(String(765))
    init = Column(String(192))
    data = Column(String)

    def __repr__(self):
        return self.name


class UsersRoles(Base):
    __tablename__ = u'users_roles'
    uid = Column(Integer, primary_key=True)
    rid = Column(Integer)


class Variable(Base):
    __tablename__ = u'variable'
    name = Column(String(384), primary_key=True)
    value = Column(String)


class ViewsDisplay(Base):
    __tablename__ = u'views_display'
    vid = Column(Integer)
    id = Column(String(192), primary_key=True)
    display_title = Column(String(192))
    display_plugin = Column(String(192))
    position = Column(Integer)
    display_options = Column(String)


class ViewsObjectCache(Base):
    __tablename__ = u'views_object_cache'
    sid = Column(String(192), primary_key=True)
    name = Column(String(96))
    obj = Column(String(96))
    updated = Column(Integer)
    data = Column(String)


class ViewsView(Base):
    __tablename__ = u'views_view'
    vid = Column(Integer, primary_key=True)
    name = Column(String(96))
    description = Column(String(765))
    tag = Column(String(765))
    view_php = Column(String)
    base_table = Column(String(96))
    is_cacheable = Column(Integer)


class Vocabulary(Base):
    __tablename__ = u'vocabulary'
    vid = Column(Integer, primary_key=True)
    name = Column(String(765))
    description = Column(String)
    help = Column(String(765))
    relations = Column(Integer)
    hierarchy = Column(Integer)
    multiple = Column(Integer)
    required = Column(Integer)
    tags = Column(Integer)
    module = Column(String(765))
    weight = Column(Integer)


class VocabularyNodeTypes(Base):
    __tablename__ = u'vocabulary_node_types'
    vid = Column(Integer)
    type = Column(String(96), primary_key=True)


class VotingapiCache(Base):
    __tablename__ = u'votingapi_cache'
    vote_cache_id = Column(Integer, primary_key=True)
    content_type = Column(String(192))
    content_id = Column(Integer)
    value = Column(Float)
    value_type = Column(String(192))
    tag = Column(String(192))
    function = Column(String(192))
    timestamp = Column(Integer)


class VotingapiVote(Base):
    __tablename__ = u'votingapi_vote'
    vote_id = Column(Integer, primary_key=True)
    content_type = Column(String(192))
    content_id = Column(Integer)
    value = Column(Float)
    value_type = Column(String(192))
    tag = Column(String(192))
    uid = Column(Integer)
    timestamp = Column(Integer)
    vote_source = Column(String(765))


class Watchdog(Base):
    __tablename__ = u'watchdog'
    wid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    type = Column(String(48))
    message = Column(String)
    variables = Column(String)
    severity = Column(Integer)
    link = Column(String(765))
    location = Column(String)
    referer = Column(String(384))
    hostname = Column(String(384))
    timestamp = Column(Integer)


class Weblinks(Base):
    __tablename__ = u'weblinks'
    nid = Column(Integer, primary_key=True)
    vid = Column(Integer, primary_key=True)
    click_count = Column(Integer)
    last_click = Column(Integer)
    weight = Column(Integer)
    last_status = Column(String(12))
    last_checked = Column(Integer)
    urlhash = Column(String(96))
    url = Column(String)
    reciprocal = Column(String)


class ContentTypeSite(Base):
    __tablename__ = u'content_type_site'
    revisions = Column('vid', Integer, ForeignKey('node.vid'), primary_key=True)
    nid = Column('nid', Integer, ForeignKey('node.nid'))
    industry_type = Column('field_industry_type_value', String(765))
    property_id = Column('field_site_id_value', String(765))
    timezone = Column('field_timezone_value', String)
    site_id = nid
    node = relationship("Node", foreign_keys=[nid])

    def __unicode__(self):
        return u'{} - {}'.format(self.node.title, self.property_id)
    __repr__ = __str__ = __unicode__


class ContentTypeImage(Base):
    __tablename__ = u'imageview'  # TODO: figure out how to create this view dynamically/if it's not there.
    id = Column('nid', Integer, primary_key=True)
    title = Column(String(255))
    site_id = Column(Integer)
    site = Column('site_id', Integer, ForeignKey('content_type_site.site_id'))
    file_mime = Column('filemime', String(255))
    file_path = Column('filepath', String(255))
    file_name = Column('filename', String(255))
    fid = Column(Integer)

    # SQL for 'imageview':
    """create view imageview as select node.nid, node.vid, node.title, files.filemime, files.filepath, files.filename, files.fid, og_ancestry.group_nid as site_id
         from content_type_image
        left join content_field_image_element using (vid)
        left join node on content_type_image.nid = node.nid
        left join files on content_field_image_element.field_image_element_fid = files.fid
        left join og_ancestry on node.nid = og_ancestry.nid;"""

    def __unicode__(self):
        return self.title
    __repr__ = __str__ = __unicode__


class PropertyUsers(Base):
    __tablename__ = u'property_users'  # TODO: figure out how to create this view dynamically/if it's not there.
    uid = Column(Integer, ForeignKey('users.uid'), primary_key=True)
    site_nid = Column(Integer, ForeignKey('content_type_site.nid'))
    property_id = Column(String(255))
    node = relationship("ContentTypeSite")
    user = relationship("Users")

    def __unicode__(self):
        return u'<Uid: {}, Site: {}>'.format(self.user.name, self.property_id)
    __repr__ = __str__ = __unicode__

if __name__ == '__main__':
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker(bind=create_engine(os.environ['SQLALCHEMY_DRUPAL_CONNECT_STRING'], echo=False))()
    # print "Nodes",
    # print(session.query(Node).all())
    # print "Users",
    # print(session.query(Users).all())
    # print "Content Type Images",
    # print(session.query(ContentTypeImage).all())
    # print "Content Type Site",
    # print(session.query(ContentTypeSite).all())
    print "Property Users",
    print(session.query(PropertyUsers).all())
